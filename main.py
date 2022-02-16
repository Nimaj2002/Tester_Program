import subprocess
from os import listdir, remove
from os.path import isfile, join


def test():
    # Students codes
    students_codes = [f for f in listdir("./all_codes") if isfile(join("./all_codes", f))]

    # Given inputs
    inputs = [f for f in listdir("./In") if isfile(join("./In", f))]

    # Expected outputs list
    outputs = [f for f in listdir("./Out") if isfile(join("./Out", f))]

    if len(students_codes) == 0 or len(inputs) != len(outputs):
        return "Invalid inputs"

    else:
        for code in students_codes:
            # Deleteting exsisted result
            remove(f"./results/{code[:-3]}.txt")
            i = 1
            passed = 0
            failed = 0
            while i <= len(inputs):
                with open(f"./In/input{i}.txt", "r") as inn:
                    # Getting input datas
                    i_data = inn.read()

                with open(f"./Out/output{i}.txt", "r") as out:
                    # Getting expexted datas
                    o_data = out.read()

                # Getting results
                r_result = subprocess.run(f"python ./all_codes/{code}", shell=True, capture_output=True, text=True, input=i_data)
                r_result = r_result.stdout

                print("in",i_data)
                print(list(o_data))
                print(list(r_result))
                # print(f"o_data\n"==r_result)
                # Comparison between expected results and real results
                with open(f"./results/{code[:-3]}.txt", "a") as result:
                    if f"{o_data}\n" == r_result:
                        result.write(f"test{i} [PASSED]\n")
                        passed += 1
                    else:
                        result.write(f"test{i} [FAILED]\n")
                        failed += 1

                i += 1

            #   Appending percentage an passed and failed
            with open(f"./results/{code[:-3]}.txt", "a") as file:
                file.write(
                    f"Final result :\nPASSED: {passed}\nFAILED: {failed}\nPERCENTAGE: {((passed * 100) / (passed + failed))}")

        return "Finished"

if __name__ == "__main__":
    print(test())
