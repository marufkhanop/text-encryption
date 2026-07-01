Title : VaultText Description: Hey there! This is my final project for CS50P . I build a simple commandline tool that lets you encrypt and decrypt text messages using a cipher system. Basically, it scrambles your message using a completely randomized alphabet (a key) so nobody else can read it and then lets you unscramble it later if you have that exact key.

I wanted to make something straightforward but actually useful.The program keeps track of characters like uppercase and lowercase letters,numbers and basic punctuation. When you run it , you get to choose if you want to lock a message up or unlock an old one.

What each file does project.py: This is where all the main code lives.It handles asking the user what they want to do, shuffling the alphabet to make a unique key,and doing the actual math to swap the letters around.It also saves your keys inside a file called key.txt so you don't accidentally lose them.

test_project.py: This is my testing file. I set it up with pytest to double-check that my functions actually work the way they are supposed to or no. It checks things like making sure the generated key is the right length, and that encrypting and decrypting a basic letter works perfectly.

requirements.txt: This just tells Python what extra tools need to be installed.Since I wrote everything using standard Python libraries,the only thing list here is pytest so that the testing file can run good.

My design choices While making this,I had to figure out what to do if someone typed a weird symbol that isn't in my alphabet string (like a # or a @). then I decided it was best to just leave those characters exactly as they are and skip over them,and not causing the program to crash or throw an error.

I also added a quick safety check when you try to decrypt a message.If you paste a key that is too short or too long, the program will immediately stop and say "Invalid key" instead of trying to run it and breaking halfway through.