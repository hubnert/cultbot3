import yaml

TREE = yaml.load("""
say: "Welcome to the Cult Institute. Do you feel a vague sense of dread?"
answers:
  Great!:
    say: Please try again later when you’re filled with existential dread.
  Just okay . . .:
    say: Do you ever feel like something is, how shall I put this, not quite right?
    answers:
      I guess so?:
        say: Are you ready to further explore this uncertainty and unveil your mithras?
      Sometimes.:
        say: I’m sensing denial. Denial is a tool taught to us by the masses to dull the truths of our pain. Are you sure you only sometimes feel like something isn’t quite right?
      All the damn time.:
		say: I can sense you’re ready for the next step. Don’t hesitate to call us today at 810-666-CULT for further assistance.
  
""")
