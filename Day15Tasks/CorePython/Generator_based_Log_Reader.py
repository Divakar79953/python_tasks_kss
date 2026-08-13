# Generator-based Log Reader

def read_logs(filename):

    with open(filename, "r") as file:
        for line in file:
            print("READ:",line.strip())
            yield line.strip()


error_count = {}

logs = read_logs("logs.txt")

for log in logs:

    if log.startswith("ERROR"):
        
        error_message = log.replace("ERROR ", "")

        if error_message in error_count:
            error_count[error_message] += 1
        else:
            error_count[error_message] = 1


print("Error Counts:")

for error, count in error_count.items():
    print(error, ":", count)
