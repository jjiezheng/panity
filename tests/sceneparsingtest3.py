from panity.xmlparser import getSceneFromXML

xml = """
<scene>
    <gameobject name="ground">
    </gameobject>
    <gameobject name="house">
        <gameobject name="door">
        </gameobject>
    </gameobject>
    <gameobject name="something">
    </gameobject>
</scene>
"""

root = getSceneFromXML(xml)
    
for go in root:
    print go
    for child in go:
        print "- "+str(child)
