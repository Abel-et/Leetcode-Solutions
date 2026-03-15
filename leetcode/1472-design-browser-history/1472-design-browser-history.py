class BrowserHistory:
    def __init__(self, homepage: str):
        # Initialize with the homepage and pointer at 0
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # 1. Clear forward history: Slice the list up to the current element
        self.history = self.history[:self.current + 1]
        
        # 2. Add the new URL and move the pointer
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        # Move back, ensuring we don't go below index 0
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward, ensuring we don't exceed the list length
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]