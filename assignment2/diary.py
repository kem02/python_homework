import traceback

# This program opens "diary.txt" for appending.
# It prompts the user for a line of input (first prompt: "What happened today?",
# then "What else?"). Each input is written to the file.
# When the user types "done for now", that line is written and the program exits.
# All this is wrapped in a try block to catch exceptions and print helpful error info.
try:
    with open("diary.txt", "a") as file:

        not_done_for_now = True
        question = "What happened today? "
        while not_done_for_now:

            new_sentence = input(question)

            if new_sentence == "done for now":
                not_done_for_now = False
                file.write("done for now" + "\n")
            else:
                file.write(new_sentence + "\n")
                question = "What else? "

            # print(new_sentence)
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(
            f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
        )
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
