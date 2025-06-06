class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app, app_memory) -> str:
        if self.is_on is False:
            return f'Turn on your phone to install {app}'
        if self.memory >= app_memory:
            self.memory -= app_memory
            self.apps.append(app)
            return f'Installing {app}'
        return f'Not enough memory to install {app}'

    def status(self) -> str:
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'



# class Smartphone:
#     def __init__(self, memory):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         self.is_on = not self.is_on
#
#     def install(self, app, app_memory):
#         if self.memory >= app_memory and self.is_on:
#             self.apps.append(app)
#             self.memory -= app_memory
#             return f"Installing {app}"
#         elif self.memory >= app_memory and not self.is_on:
#             return f"Turn on your phone to install {app}"
#         else:
#             return f"Not enough memory to install {app}"
#
#     def status(self):
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"



smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
