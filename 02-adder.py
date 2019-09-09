# adder.py

from typing import Dict, Tuple

# More powerful turing Machine
# Simulating addition operation

ADDER_TAPE: Dict = {
    # Input to the machine
    ("#", "s1") : ("(", "R", "s2"),
    ("#", "s2") : ("1", "R", "s3"),
    ("#", "s3") : ("1", "R", "s4"),
    ("#", "s4") : ("1", "R", "s5"),
    ("#", "s5") : ("+", "R", "s6"),
    ("#", "s6") : ("1", "R", "s7"),
    ("#", "s7") : ("1", "R", "s8"),
    ("#", "s8") : (")", "R", "s9"),

    # Instruction to the machine
    ("#", "s9") : ("#", "L", "s9"),
    (")", "s9") : (")", "L", "s9"),
    ("1", "s9") : ("1", "L", "s9"),
    ("+", "s9") : ("1", "R", "s10"),

    ("1", "s10") : ("1", "R", "s10"),
    (")", "s10") : ("#", "L", "s11"),

    ("1", "s11") : (")", "R", "s12"),

    ("#", "s12") : ("#", "R", "s12"),
}


def simulate(instructions: Dict) -> None:
    """
    Simulate Turing machine based on the instruction provided
    on the tape

    Infinite Blank "#" Tape -> ...################...
    Our input to the machine -> (♞♞♞+♞♞)#############... ->  (♞♞♞♞♞)##########
    or Abstractly our input to the machine can be -> (^^^+^^)######... -> Output should be (^^^^^)######...
    or Input -> (111+11)######... -> Output should be (11111)######... i.e The unary representation of the number system
    1 -> 1
    2 -> 11
    3 -> 111
    Though it may seem simple it has to actually simulate and process the output,
    Not just hack (cut) the tape (i.e the input )
    

    eg:
    >>> simulate({('#', 's1'): ('(', 'R', 's2'),
    ...  ('#', 's12'): ('#', 'R', 's12'),
    ...  ('#', 's2'): ('1', 'R', 's3'),
    ...  ('#', 's3'): ('1', 'R', 's4'),
    ...  ('#', 's4'): ('1', 'R', 's5'),
    ...  ('#', 's5'): ('+', 'R', 's6'),
    ...  ('#', 's6'): ('1', 'R', 's7'),
    ...  ('#', 's7'): ('1', 'R', 's8'),
    ...  ('#', 's8'): (')', 'R', 's9'),
    ...  ('#', 's9'): ('#', 'L', 's9'),
    ...  (')', 's10'): ('#', 'L', 's11'),
    ...  (')', 's9'): (')', 'L', 's9'),
    ...  ('+', 's9'): ('1', 'R', 's10'),
    ...  ('1', 's10'): ('1', 'R', 's10'),
    ...  ('1', 's11'): (')', 'R', 's12'),
    ...  ('1', 's9'): ('1', 'L', 's9')}
    ... )
      s1: ################
          ^
      s2: (###############
           ^
      s3: (1##############
            ^
      s4: (11#############
             ^
      s5: (111############
              ^
      s6: (111+###########
               ^
      s7: (111+1##########
                ^
      s8: (111+11#########
                 ^
      s9: (111+11)########
                  ^
      s9: (111+11)########
                 ^
      s9: (111+11)########
                ^
      s9: (111+11)########
               ^
      s9: (111+11)########
              ^
      s10: (111111)########
                ^
      s10: (111111)########
                 ^
      s10: (111111)########
                  ^
      s11: (111111#########
                 ^
      s12: (11111)#########
                  ^
      s12: (11111)#########
                   ^
      s12: (11111)#########
                    ^
      s12: (11111)#########
                     ^
      s12: (11111)#########
                      ^
      s12: (11111)#########
                       ^
      s12: (11111)#########
                        ^

    :param instructions: Dictionary of input and instructions for the Turing machine
    :return: None

    """
    tape, head, state = ["#"] * 16, 0, "s1"

    for _ in range(24):
        print(state.rjust(4) + ": " + "".join(tape))
        print("      " + " " * head + "^")

        tape[head], head_dir, state = instructions[(tape[head], state)]
        head += 1 if head_dir == "R" else -1


simulate(ADDER_TAPE)