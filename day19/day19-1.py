# https://adventofcode.com/2023/day/19
import os
import datetime as dt

def solve(lines):
    
    functions = {"A": [["A"]], "R": [["R"]] }
    parts = []
    read_fns = True
    for line in lines:
        if line=="":
            read_fns = False
            continue
        if read_fns:
            # read the rules
            #px{a<2006:qkq,m>2090:A,rfg}
            temp=line.split("{")
            fn=temp[0]
            rules=temp[1][:-1]
            functions[fn] = [r.split(":") for r in rules.split(",")]
        else:
            # read the parts
            #{x=787,m=2655,a=1222,s=2876}
            part={}
            for feature in line[1:-1].split(","):
                xmas,val=feature.split("=")
                part[xmas] = val
            parts.append(part)

    res=0
    for part in parts:
        accepted=rejected=False
        fn="in"
        while not accepted and not rejected:
            rules = functions[fn]
            for rule in rules:
                if rule[0] in ("A","R"):
                    accepted=rule[0]=="A"
                    rejected=rule[0]=="R"
                    break
                if len(rule)==1:
                    fn=rule[0]
                    break
                test_rule=rule[0]
                for c in "xmas":
                    test_rule = test_rule.replace(c,str(part[c]))
                rule_applies = eval(test_rule)
                if rule_applies:
                    fn=rule[1]
                    break
        if accepted:
            res+=sum(map(int,part.values()))

    return res

def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines)
    print(f"The result is {result}.")
    # 391132

start_t = dt.datetime.now()
main(test=True)

start_t = dt.datetime.now()
main(test=False)
end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")