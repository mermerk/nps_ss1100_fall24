# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems

### Merkley	Ryan (Kelly)	Rubio Castaneda	Raves

### Assignment
- **Instructions**: Work in groups of four to complete the steps outlined in the project instructions.
- **Submission**: All of your submission will go here in this repository, to include this README file to hold your writeup.

### Procedure
#### Preparation
- Employ programming skills to solve problems related to spacecraft subsystems.
- Develop code and responses to tasks in various sections.
- Experience working with code and collaborating on a coding project.

#### Requirements
1. Complete all tasks listed in each section, paying attention to the Evaluation subsections.
2. Use MatLab to complete at least one of the tasks.
3. Submit the project using GitHub, replacing the content of this README file with your writeup and presentation of the work.

#### Subsystems and Tasks
Reaction Control Subsystem (RCS): Malfunction detection and velocity change calculation.\
Thermal Control Subsystem (TCS): Temperature control function.\
Attitude Control Subsystem (ACS): Attitude determination and rotation calculations.\
Command and Data Handling (C&DH): Command parsing and routing.\
Electrical Power Subsystem (EPS): Power budget analysis and battery charging calculations.\
Remote Sensing Payload: Data ingestion, radiance to reflectance conversion, and image rescaling.

1. What was your experience in collaborating? Talk about what steps you used to ensure the
inputs from group members worked - code testing, GitHub branch management, etc. - and
how you divided up the workload for the project.
We divided up the various sections and then met in person twice to bounce ideas off of each other and assist in answering questions everyone had with their various assigned codes.

2. What was the most challenging section, and why? Feel free to provide more than one response
if there is a difference of opinion in the group. Remote Sensing.  It used file import, matrix operations, no value "error handling", and multiple library-specific functions.
Command Parsing was also complicated based on the syntax needed to align the inputs (also ensuring the correct input format was used) with the values embedded in the dictionary. 

4. If you employed Generative AI tools, how did you do so? Discuss which tools you used, the
prompts you utilized, how you ensured the results were valid, and how you integrated the code
into your tasks.
ChatGPT was a helpful tool to verify the code generated was sound.  Also, using prompts like "how could I improve this line of code?".  It is also a very efficient way to learn new information, like "explain what a -1 stack axis means".  It is often much faster than googling it and pouring over the 'forums' for a useful explanation.  The same can be said for generating code as well, "how do I display the data containing in [x,y,z] as an image?"

5. What other resources did you use to find solutions? Online sites, books, references, etc.

6. In what way could this project be improved for future quarters?
Use github from the beginning of the course with the assigned labs in order to increase familiarization and ease of use. We ran into a few technical problems, trying to understand how github was structured. Having exposure to this earlier would be helpful, and would make collaboration with the other labs easier. 


# Instructor Comments

### ADC
The simplicty of your code was excellent. Good comments, good use of compact Python syntax - great programming.

### C&DH 
Great use of string methods to "clean up" the inputs before going into your functions. A few of the variables you used were just "renaming" existing variables, which is usually frowned upon since it doesn't add much to your code. I get that sometimes you want to use a parameter or variable differently later in the code, so one way to deal with this is to break up your script into smaller, self-contained functions. The output of one function would then feed into the next. Not only is this more modular and easier to develop, it also avoids cascading errors that might occur when multiple variables point "back through" each other recursively to the same value.

### EPS
Great use of matlab. Do be careful with all of the string methods at the end. I get that you were using them to make sure that the data would work in Matlab, but they're so specific that if anything changes in the inputs it will end up being a big mess to figure out how to adapt all of the strip and replace operations.
