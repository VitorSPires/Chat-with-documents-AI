with open("Temp_Manual-CAM_ES.txt", "r", encoding="utf-8") as input:
    input_ = input.read().split("\n\n")   #\n\n denotes there is a blank line in between paragraphs.


for i in input_:
    print(i)
    print('---------------')