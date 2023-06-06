morse_code = {
    'A': '.-', 'B':'', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L':'', 'M':'', 'N': '','O': '', 'P': '', 'Q': '', 'R':'', 'S':'', 'T':'','U':'','V':'','W':'', 'X':'', 'Y':'', 'Z':'',
  
}

def convert_to_morse_code(text):
  morse_code_text = ""
  for char in text.upper():
    if char in morse_code:
      morse_code_text += morse_code[char] + " "
    else:
      morse_code_text += char
   return morse_code_text

user_input = input("Enter a string: ")
morse_code_output = convert_to_morse_code(user_input)
print("Morse code output:", morse_code_output)
