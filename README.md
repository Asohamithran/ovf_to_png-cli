# ovf_to_png-cli
### This cli uses the ovf parser library to convert .ovf (OOMMF vector files) to .png.
 Useful for rapid testing of .ovf file
# Dependencies 
ovf parser library for spirit code: https://github.com/spirit-code/ovf
# Usage:
`python ovf_test.py file_name.ovf`
# output .png images
![spin configuration](https://github.com/Asohamithran/ovf_to_png-cli/blob/main/spin%20data%20header-4.png)
![spin configuration](https://github.com/Asohamithran/ovf_to_png-cli/blob/main/spin%20data%20header-8.png)

# Making the cli executable 
ovf_test.py can be marked as an executable with the following command 
`chmod +x ovf_test.py`
## add the cli to $PATH
Add the directory containing the script to the $PATH variable, to keep the change
add the `export PATH=/path/to/script:$PATH` to `.bashrc`or `bash_profile`
