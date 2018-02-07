import json
from odf.opendocument import OpenDocumentText
from odf.namespaces import OFFICENS
from odf.text import P, LineBreak
from odf.office import Annotation, AnnotationEnd
from odf.dc import Creator
from odf.element import Element

# annotations begin and end
def create_anno_begin(type_, id_, properties):
    a = Annotation()
    a.setAttrNS(OFFICENS, 'name', str(id_))
    a.addElement(Creator(text=type_))
    a.addElement(P(text=json.dumps(properties, indent=2)))
    return a

def create_anno_end(id_):
    return AnnotationEnd(name=str(id_))

# 'begin'
# 'end'
# 'type'
# 'properties'
def to_odf(text, annotations, outputfile):
    anno_parts_index = {}
    id_ = 0
    for a in annotations:
        begin = a['begin']
        end = a['end']
        if begin not in anno_parts_index:
            anno_parts_index[begin] = []
        if end not in anno_parts_index:
            anno_parts_index[end] = []
        anno_parts_index[begin].append(create_anno_begin(a['type'], id_, a['properties']))
        anno_parts_index[end].append(create_anno_end(id_))
        id_ += 1
    # create final list with text blocks
    comps = list(text)
    comps.append(None) # for eventual annotation
    for i in reversed(range(0, len(text) + 1)):
        if comps[i] == '\r':
            comps[i] = ''
        if comps[i] == '\n':
            comps[i] = LineBreak()
        if i in anno_parts_index:
            for a in anno_parts_index[i]:
                comps.insert(i, a)
    # generate document structure
    p = P()
    last_string_index = None
    for i, v in enumerate(comps):
        if isinstance(v, str):
            if last_string_index is None:
                last_string_index = i
        else:
            if last_string_index is not None:
                p.addText(''.join(comps[last_string_index:i]))
                last_string_index = None
            if isinstance(v, Element):
                p.addElement(v)
    doc = OpenDocumentText()
    doc.text.addElement(p)
    doc.save(outputfile)
