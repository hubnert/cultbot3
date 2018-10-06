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
        say:  I’m sensing denial. Denial is a tool taught to us by the masses to dull the truths of our pain. Are you sure you only sometimes feel like something isn’t quite right?
      All the damn time.:
        say: I can sense you’re ready for the next step. Don’t hesitate to call us today at 810-666-CULT for further assistance.
  Terrible!:
    say: Are you just saying that because you think it's what we want to hear?
    answers:
		No seriously. Life is a fraught mess.
			say: I'm glad to see that you've pierced the veil that society has drawn over your eyes. But the real question is, are you ready to do something about it?
			answers:
				Hell yes.
					say: I can sense you’re ready for the next step. Don’t hesitate to call us today at 810-666-CULT for further assistance.
				It sounds like a lot of work.
					say: I understand your hesitation but nothing good in life has ever come easy. Do a little thinking on that and come back to us at a later date.
		Um. Maybe?
			say: We're looking for followers who are leaders. Not followers who are follwers. If you're not ready to take control, you're not ready for Cult Institute.
      
""")
