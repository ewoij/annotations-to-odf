from annos_to_odf import to_odf

text = 'How is it going in Hawaii?'

annotations = [{
    'begin': 19,
    'end': 25,
    'type': 'NamedEntity',
    'properties': {
        'type': 'Location'
    }
}]

to_odf(text, annotations, 'helloworld.odt')
