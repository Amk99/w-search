import os

def search_words_in_logs(word_list, log_folder, output_folder):
    if not os.path.exists(log_folder):
        print(f"Log folder '{log_folder}' doesn't exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for log_file in os.listdir(log_folder):
        if log_file.endswith('.log'):
            log_path = os.path.join(log_folder, log_file)
            with open(log_path, 'r') as log:
                lines_with_words = [line.strip() for line in log if any(word in line for word in word_list)]
                if lines_with_words:
                    output_path = os.path.join(output_folder, f"{log_file}_results.txt")
                    with open(output_path, 'w') as output_file:
                        output_file.write('\n'.join(lines_with_words))

if __name__ == "__main__":
    search_words = ["error", "warning", "critical"]
    logs_folder = "D:\\test"
    output_folder = "D:\\res"

    search_words_in_logs(search_words, logs_folder, output_folder)

    print("Results saved in separate files.")
