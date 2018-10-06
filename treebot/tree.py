import yaml

TREE = yaml.load("""
say: "Hello there, and welcome to Cult.Institute. Today I’ll be your psychical advisor. By the end of our session, I’ll have evaluated your current levels of dread and woe, and I’ll be able to recommend what you should do next. Let’s begin. How are you?"
answers:
  Great!:
    say: Please try again later when you’re filled with existential dread.
    answers:
		Thanks for nothing
			say: When you can learn to let the darkness in, we’ll be here to bring back the light. Good bye.
		But I want in!
			say: We’re not just a cult of popularity. Try again later when you begin to take this seriously. Good bye.
		 I only said that because I feel like I’m supposed to.
		  say: I’m glad you can finally be honest with yourself. I recommend you contact us for further assistance at 810-666-CULT. Good bye.
  Just okay . . .:
    say: Do you ever feel like something is, how shall I put this, not quite right?
    answers:
      I guess so?:
        say: Are you ready to further explore this uncertainty and unveil your mithras?
		answers:
			Absolutely!
				say: I can sense you’re ready for the next step. Don’t hesitate to call us today at 810-666-CULT for further assistance.
			Maybe, but I’m afraid.
				say:Fear is what’s holding you back! We were once afraid too, just like you. Join us to slay your mithras and unleash your true potential. Call us today at 810-666-CULT.
      Sometimes.:
        say: I’m sensing denial. Denial is a tool taught to us by the masses to dull the truths of our pain. Are you sure you only sometimes feel like something isn’t quite right?
      All the damn time.:
        say: You need a Study Visa (Tier 4)
  Terrible!:
    say: How long are you going to stay in the UK? up to 6 months; more than 6 months
    answers:
      up to 6 months:
        say: You need a Standard Visitor Visa
      more than 6 months:
        say: Are you an 1. entrepreneur 2.investor 3. leader in arts or sciences 4. none of the above
        answers:
          '1':
            say: You can apply for a Tier 1 Entrepreneur
          '2':
            say: You can apply for Tier 1 Investor
          '3':
            say: You can apply for Tier 1 (Exceptional Talent)
          '4':
            say: Are you offered  1. a skilled job 2. role in the UK branch of your employer 3. job in a religious community 4. job as an elite sportsman or coach
            answers:
              '1':
                say: You can apply for a Tier 2 (General) visa
              '2':
                say: You can apply for a Tier 2 (Intra-company transfer)
              '3':
                say: Tier 2 (Minister of Religion)
              '4':
                say: Tier 2 (Sportsperson)
""")
