import string
def input_data_handler(input_data:str, g = None)->str:
    """ОБработка входных конфигурационных данных"""
    if g == "None":
        input_data = input("Повторите ещё раз")
    else:
        if input_data == "д" or input_data == "Д":
            result_string = "Включено!"
            g = "True" 
            return [input_data, result_string, g]
        elif input_data == "н" or input_data == "Н":
            result_string = "Не включено!"
            g = "False"
            return [input_data, result_string, g]
        elif input_data == "Сброс":
            result_string = "Сброс!"
            g = "Break"
            return "break"
        else:
            result_string = "Ответ не распознан"
            g = "None"
            return [input_data, result_string, g, input_data_handler(input_data)]


high_register = str(input("Высокий регистр, должен быть включен?(Д/н?)"))
result_high_register = input_data_handler(high_register)
print(result_high_register)
low_register = str(input("Нижний регистр, должен быть включен?(Д/н?)"))
result_low_register = input_data_handler(low_register)
print(result_low_register)
numbers = str(input("Числа должны быть включены(Д/н?)?"))
result_numbers = input_data_handler(numbers)
print(result_numbers)
symbols = str(input("Символы должны быть включены(Д/н?)?"))
result_symbols = input_data_handler(symbols)
print(result_symbols)

if result_high_register and result_low_register and result_numbers and result_symbols == "Не вклюено, ВООООООООООООООООООООБЩЕ!":
    print("Ошибка.")
else:
    if result_high_register == "Включено!":
        method1 = string.ascii_uppercase()
    if result_low_register == "Включено!":
        method2 = string.ascii_lowercase()
    if result_numbers == "Включено!":
        method3 = string.digits()
    if result_symbols == "Включено!":
        method4  = string.punctuation()
    