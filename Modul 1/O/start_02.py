class Logger:
    def log_to_console(self, message):
        print(message)

    def log_to_file(self, message, file_name):
        with open(file_name, 'w') as file:
            file.write(message)