from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(direction, text, shift):
  coded_text = ""
  if direction == 'decode':
    shift *= -1
  
  for letter in text:
    if letter in alphabet:
      alpha_idx = alphabet.index(letter)
      coded_text += alphabet[(alpha_idx+shift)%26]
    else:
      coded_text += letter
  
  print(f"The {direction}d text is {coded_text}")

print(logo)
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(direction, text, shift)

  again = input("Type \"yes\" if you want to again. Otherwise, type \"no\": \n").lower()
  if again == 'no':
    print("Thank you for using Caesar Cipher!")
    break
  
