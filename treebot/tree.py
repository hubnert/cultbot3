import yaml

TREE = yaml.load("""
say: "Welcome to the Cult Institute. Do you feel a vague sense of dread?"
answers:
  i think so:
    say: https://media.giphy.com/media/4pMX5rJ4PYAEM/giphy.gif
  not really?:
    say: How long are you going to stay in the UK? up to 6 months; more than 6 months
    answers:
      up to 6 months:
        say: You can apply for a Short-term Study Visa
      more than 6 months:
        say: You need a Study Visa (Tier 4)
  
""")
