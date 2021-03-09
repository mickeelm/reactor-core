import json
import re

regex = re.compile("`[^`]*`")

with open("mapping.json") as mapping_file:
    mapping = json.loads(mapping_file.read())

with open("giggity") as old, open("giggity.adoc", "w") as new:
    for line in old.readlines():
        matches = regex.findall(line)
        for match in matches:
            stripped = match.strip("`")
            if stripped in mapping:
                links = mapping[stripped]
                if links:
                    if len(links) == 1:
                        line = line.replace(match, "{}[{}]".format(links[0], stripped))
                    else:
                        line = line.replace(match, "{} ({}[Flux]|link:{}[Mono])".format(match, links[0], links[1]))
                else:
                    print("No link for {}".format(stripped))
            else:
                print("NO MAPPING for {}!".format(stripped))
        new.write(line)
