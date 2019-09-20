# qc-sim
A quantum computer simulator.

## Eval() is used in this program!

This code currently uses eval() in the custom_gate() function to allow users to input complex numbers, square roots, &c as entries for their gates. HOWEVER, the inputs going into eval() are sanitized - stripped of all quotation marks, forward slashes, and backward slashes. If you believe this is not sufficient sanitization, please open an issue.

## Using the simulator

### Overview

This quantum computer simulator allows users to simulate systems of any number of qubits (or at least, as many as your computer's processing power allows), apply custom gates, and measure the qubits, while providing information about the probability of different outcomes and the current state of the computer. It is entirely text based - if you're looking for nice graphics, try quirk or the IBM simulator, though there are some features of this simulator neither of those offer.

### Runtime

Once cloned, run file labeled fresh-qc-sim.py. If you want to experiment, I suggest using the standard interface; in this case, type in 'cli' when it asks. (If you are running more regular tests/are more familiar with quantum computers, the 'file' input option may be the best for you - skip further down.) It will begin by asking you how many qubits you'd like to use - feel free to input any number, though again, you will be limited by your computer's abilities. You can then start in the 0 or 1 state. When it asks 'ideal or nonideal' please enter 'ideal' as the nonideal capabilities are currently being designed/programmed. You can then select the options it provides - importing gate, measuring your qubits (either one individual qubit or all of them), entering a custom gate (which you can then save to import in another run if you so choose), or using a previously imported or created gate. It will show you the state of your system after every operation you perform, and inquire if you'd like to do more. When you are done, it will provide the probability of each basis state being the result upon measurement and the final state.

The code will output a file as well, titled by the date and time you ran the simulator at, with what you inputted and what the result was.

Please note that if you put gibberish in when an input is requested, python will give you an error - with very few exceptions, I haven't written code to sanitize user inputs. If this is actually a problem for you/your uses, feel free to start an issue.

### File input

If you are already pretty familiar with quantum computers and are using this simulator to test algorithms, this simulator also accepts a file as input (effectively, a program for the simulator engine). The format is as follows:

Line 1 - number of qubits
Line 2 - ideal or nonideal simulation
Line 3 - starting state (|0> or |1>)

After this header, each new line must be one of two things. It can be a file that contains a gate saved in the numpy format (the file gate_calc.py saves them appropriately, as does the custom option in the standard interface of the simulator). For example, you might type 'hadamard4x4.txt' (without the quotation marks). It can also be the word 'measure' followed either by 'all' (if you want to measure the whole state) or the number of the qubit you wish to measure. An example program follows:

````
2
ideal
0
hadamard4x4.txt
measure 1
not4x4.txt
````
There will be minimal print output if you do this. It will output the end state, and also produce a file you can open that contains what you ran, the end state, and the date and time you ran it.

### Generating custom gates

The file gate_calc.py allows users to input any size matrix and scale it for use on larger numbers of qubits. This can be very useful for calculating custom gates. You can then directly save these gates and then import them during runtime of the simulator.

## Soon to be added features
The nonideal section is a more longterm feature which will incorporate a noise function to simulate decoherence and allow researchers to test error correction systems and get a better idea of how their algorithms will run on a real quantum computer. I'm also working on uploading a folder of starter gates so people can immediately start working with the simulator.

## Errors? Features you want?

Please create an issue so that I can address them!
