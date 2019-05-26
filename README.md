# qc-sim
A quantum computer simulator.

## Eval() is used in this program!

This code currently uses eval() in the custom_gate() function to allow users to input complex numbers, square roots, &c as entries for their gates. This will probably eventually be changed to a safer custom parser, but for now it will be eval(). Please do not download this to something that has public access. 

## Using the simulator

### Overview

This quantum computer simulator allows users to simulate systems of any number of qubits (or at least, as many as your computer's processing power allows), apply custom gates, and measure the qubits, while providing information about the probability of different outcomes and the current state of the computer. It is entirely text based - if you're looking for nice graphics, try quirk or the IBM simulator, though there are some features of this simulator neither of those offer.

### Runtime

Once cloned, run file labeled fresh-qc-sim.py. It will begin by asking you how many qubits you'd like to use - feel free to input any number, though again, you will be limited by your computer's abilities. You can then start in the 0 or 1 state. When it asks 'ideal or nonideal' please enter 'ideal' as the nonideal capabilities are currently being designed/programmed. You can then select the options it provides - importing gate, measuring your qubits (either one individual qubit or all of them), entering a custom gate (which you can then save to import in another run if you so choose), or using a previously imported or created gate. It will show you the state of your system after every operation you perform, and inquire if you'd like to do more. When you are done, it will provide the probability of each basis state being the result upon measurement and the final state.

Please note that if you put gibberish in when an input is requested, python will give you an error - with very few exceptions, I haven't written code to sanitize user inputs. If this is actually a problem for you/your uses, feel free to start an issue.

### Generating custom gates

The file gate_calc.py allows users to input any size matrix and scale it for use on larger numbers of qubits. This can be very useful for calculating custom gates. One feature that I need to add here is the ability to save these generated gates in the proper format for importing in the main simulator; currently you need to calculate it and then type in the result element by element in the custom gate option of fresh-qc-sim.py.

## Soon to be added features

I'm currently working on adding a custom parser to the inputs for custom gates so that `eval()` will not be used. The nonideal section is a more longterm feature which will incorporate a noise function to simulate decoherence and allow researchers to test error correction systems and get a better idea of how their algorithms will run on a real quantum computer.

## Errors? Features you want?

Please create an issue so that I can address them!
