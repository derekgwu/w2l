class W2L:
    def __init__(self):
        self.map = {
            "cls": "clear",
            "dir": "ls",
            "find": "grep",
            "chdir" : "pwd",
            "move" : "mv",
            "time" : "date",
            
        }

    def display_mapping(self):
        print("*********************")
        print(f"| {'Windows':<10} | {'Linux':>5} |")
        print("---------------------")

        for windows_cmd, linux_cmd in self.map.items():
            print(f"| {windows_cmd:<10} | {linux_cmd:>5} |")

        print("*********************")

    def main(self, args):
        if len(args) == 1:
            self.display_mapping()

        elif len(args) == 3:
            if args[1] == "-w":
                windows_cmd = args[2]
                linux_cmd = self.map.get(windows_cmd, "Unknown")
                print(f"Linux equivalent of '{windows_cmd}': {linux_cmd}")
            if args[1] == "-l":
                linux_cmd = args[2]
                windows_cmd = next((win for win, lin in self.map.items() if lin == linux_cmd), "Unknown")
                print(f"Windows equivalent of '{linux_cmd}': {windows_cmd}")
        else:
            print(len(args))
            print("Invalid arguments")



if __name__ == "__main__":
    import sys
    instance = W2L()
    instance.main(sys.argv[1:])
