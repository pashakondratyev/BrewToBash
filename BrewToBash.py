#BrewToBash
#Pavel Kondratyev
#Takes a Brewfile in the main directory and turns it into a shell script


#Prereqs: There exists a Brewfile in the current working directory
def main():
    outputFile = open( 'brew.sh', 'w' )
    inputFile = open( 'Brewfile', 'r' )
    #Header
    outputFile.write("""#!/bin/bash
#Install Homebrew if not installed
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
#Update Homebrew    
brew update         
#Upgrade existing   
brew upgrade --all  
            \n""")
    for line in inputFile:
        index = line.find("'")
        if(line[0] == 't'):     #t corresponds to tap
            outputFile.write("brew tap " + str(line[index:]))
        elif(line[0] == 'b'):   #b corresponds to brew
            outputFile.write("brew install " + str(line[index:]))
        elif(line[0] == 'c'):   #c corresponds to cask
            outputFile.write("brew cask install " + str(line[index:]))
    outputFile.write("""#Cleanup install files
brew cleanup
brew cask cleanup""")
    outputFile.close()
    inputFile.close()

if __name__ == "__main__":
    main()
