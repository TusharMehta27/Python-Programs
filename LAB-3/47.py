'''Consider the following dictionary stateCapital:
stateCapital = {&quot;AndhraPradesh&quot;:&quot;Hyderabad&quot;, &quot;Bihar&quot;:&quot;Patna&quot;,
&quot;Maharashtra&quot;:&quot;Mumbai&quot;,&quot;Rajasthan&quot;:&quot;Jaipur&quot;}
Find the output of the following statements:
i. print(stateCapital.get(&quot;Bihar&quot;))
ii. print(stateCapital.keys())
iii. print(stateCapital.values())
iv. print(stateCapital.items())
v. print(len(stateCapital))
vi print(&quot;Maharashtra&quot; in stateCapital)
vii. print(stateCapital.get(&quot;Assam&quot;))
viii. del stateCapital[&quot;Rajasthan&quot;]'''

stateCapital = {"AndhraPradesh": "Hyderabad", "Bihar": "Patna", "Maharashtra": "Mumbai", "Rajasthan": "Jaipur"}
print(stateCapital.get("Bihar"))
print(stateCapital.keys())
print(stateCapital.values())
print(stateCapital.items())
print(len(stateCapital))
print("Maharashtra" in stateCapital)
print(stateCapital.get("Assam"))
del stateCapital["Rajasthan"]
