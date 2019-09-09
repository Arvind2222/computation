from typing import Dict
X_B = {
	("B", "s1"): ("X", "R", "s2"),
	("B", "s2"): ("B", "L", "s3"),
	("X", "s3"): ("B", "R", "s4"),
	("B", "s4"): ("B", "L", "s1"),
}

def simulate(instructions: Dict) -> None:
	"""
	An XB Machine, Sees X Changes to B, Sees B Changes to X
	Simplest Turing Machine possing with limited tape.

	>>> simulate({('B', 's1'): ('X', 'R', 's2'),
	...  ('B', 's2'): ('B', 'L', 's3'),
	...  ('B', 's4'): ('B', 'L', 's1'),
	...  ('X', 's3'): ('B', 'R', 's4')} )
	
	  s1: BB
	      ^
	  s2: XB
	       ^
	  s3: XB
	      ^
	  s4: BB
	       ^
	  s1: BB
	      ^
	  s2: XB
	       ^
	  s3: XB
	      ^
	  s4: BB
	       ^
	       
	:param instructions: A dictionary of tuple as an instruction for the machine to run.
	:return: None [Process -> A String output of the simulation.]
	"""
	tape, head, state = ["B", "B"], 0, "s1"
	
	for _ in range(8):
		print(state.rjust(4) + ": " + "".join(tape))
		print("      " + " " * head + "^")
		
		tape[head], head_dir, state = instructions[(tape[head], state)]
		head += 1 if head_dir == "R" else -1
		
simulate(X_B)

