def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    # Your code here

    def code_map(map_from, map_to):
        mapped_dict = {}
        for i in range(len(map_from)):
            mapped_dict[map_from[i]] = map_to[i]

        return mapped_dict

    def decode(mapped_dict, code):
        output = []
        for e in code:
            output.append(mapped_dict[e])

        output_str = ''
        output_str = output_str.join(output)
        return output_str

    key_code = code_map(map_from,map_to)

    decoded = decode(key_code,code)

    return (key_code, decoded)


print(cipher('abc', 'def', 'aabbccbbaa'))

print(cipher('aims', 'maty', 'miaas'))