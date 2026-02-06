import shutil
import os

def check_disk_usage():
    # Get stats for the Termux home directory
        total, used, free = shutil.disk_usage("/")

            print("--- 📱 Termux System Check ---")
                print(f"Total Space: {total // (2**30)} GB")
                    print(f"Used Space:  {used // (2**30)} GB")
                        print(f"Free Space:  {free // (2**30)} GB")

                            percent = (used / total) * 100
                                print(f"Storage Usage: {percent:.1f}%")

                                if __name__ == "__main__":
                                    check_disk_usage()
                                    