import sys

# Statically-typed languages are superior,
# change my mind.
input = sys.stdin.read()
punctuation = '.!?'
uppers = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ'
lowers = 'abcdefghijklmnñopqrstuvwxyzü'
output = ''
iter = -1
skip = False

# If you won't give me curly brackets
# I'll make my own.
for c in input:
# {
    # Why did they have to remove
    # pre- and post-incrementing?
    iter += 1

    # There is a better way to do this
    # but this is easier.
    if (skip):
        output += '\n'
        skip = False
        continue

    # I can't forget to add this.
    output += c
    
    # This syntax pains my soul deeply.
    if (c not in punctuation): continue

    # Why r, you might ask. Well, it is because
    # we don't want to cause out-of-range errors
    # when we test to see if this really is
    # the end of a sentence later.
    r = 9
    if (iter + 1 + r >= len(input) - 1): continue

    # If this is either a '!' or a '?', we're
    # just gonna assume it is the end of the
    # sentence even though there might be some
    # tomfoolery going on. Oh well.
    if (c in '!?'):
    # {
        skip = True
        continue
    # }

    # Now we're cooking with gas.
    if (input[iter + 1] == ' '):
    # {
        # Now the shenanigans begins.
        # We have to check for situations where
        # we have a Ms. or a Mrs. or something
        # followed by a name.
        # We also should check if we have a
        # short abbreviation followed by some
        # long abbreviation such as PhD or
        # STD or something equally awful.
        eos = True
        per = False
        cap = False
        for i in range(r):
        # {
            # Let's grab our letter.
            cn = input[iter + 1 + i]

            # If we run into a '!' or a 
            # '?' then we're just going to
            # assume the preceding '.' was
            # an abbreviation.
            if (cn in '!?'):
            # {
                eos = False
                break
            # }

            # If we run into another something
            # that isn't a capital we assume
            # that we've run into an
            # abbreviation issue.
            if ((cn in lowers) and not cap):
            # {
                eos = False
                break
            # }

            # If we run into another period,
            # let's take note of that.
            if (cn == '.'):
            # {
                per = True
                continue
            # }

            # If this character is a capital and
            # so was the preceding one, assume we're
            # dealing with some Roman numeral weirdness
            # and say not 'eos.'
            if (cap and (cn in uppers)):
            # {
                eos = False
                break
            # }
            
            # If this character was preceded
            # by a capital and a period then
            # if this is a capital, we'll
            # assume we're dealing with a
            # name and abbreviation situation
            # and treat it as an eos.
            if (per and cap and cn in uppers): break
            
            # If we run into a capital
            # let's also take note of that.
            if (cn in uppers): cap = True
        # }

        if (eos): skip = True
    # }
# }

print(output)