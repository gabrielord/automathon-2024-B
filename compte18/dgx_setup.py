import os
import sys

# copy an SSH private and public keys to the user's home directory
def copy_ssh_keys(account_number=1):
    home_dir = os.path.expanduser("~")
    ssh_dir = os.path.join(home_dir, ".ssh")
    if not os.path.exists(ssh_dir):
        os.makedirs(ssh_dir)
    private_key = os.path.join(ssh_dir, "id_rsa_dgx")
    public_key = os.path.join(ssh_dir, "id_rsa_dgx.pub")
    if not os.path.exists(private_key):
        # check if os is windows
        if os.name == 'nt':
            os.system(f"copy compte{account_number} " + private_key)
            os.system("chmod 600 " + private_key)
        else:    
            os.system(f"cp compte{account_number} " + private_key)
    if not os.path.exists(public_key):
        # check if os is windows
        if os.name == 'nt':
            os.system(f"copy compte{account_number}.pub " + public_key)
        else:    
            os.system(f"cp compte{account_number}.pub " + public_key)

# edit the ssh config file to use the copied keys
def edit_ssh_config(account_number=1):
    home_dir = os.path.expanduser("~")
    ssh_dir = os.path.join(home_dir, ".ssh")
    config_file = os.path.join(ssh_dir, "config")
    user = f"compte{account_number}"
    if not os.path.exists(config_file):
        with open(config_file, "w") as f:
            f.write("Host dgx\n")
            f.write("    HostName hubia-dgx.centralesupelec.fr\n")
            f.write("    IdentityFile ~/.ssh/id_rsa_dgx\n")
            f.write(f"    User {user}\n")
    else:
        with open(config_file, "a") as f:
            f.write("Host dgx\n")
            f.write("    HostName hubia-dgx.centralesupelec.fr\n")
            f.write("    IdentityFile ~/.ssh/id_rsa_dgx\n")
            f.write(f"    User {user}\n")

# main function
def main():
    print("Hello! Welcome to the DGX setup script.\n This script will copy your SSH keys to your home directory and edit the SSH config file to use the copied keys.")
    account_number = int(input("Please enter your account number: "))
    print("Copying SSH keys...")
    copy_ssh_keys(account_number)
    print("Done.")
    print("Editing SSH config file...")
    edit_ssh_config(account_number)
    print("Done.")
    print("You are all set! You can now connect to the DGX server by typing 'ssh dgx' in your terminal.")

if __name__ == "__main__":
    main()

