# Annotations to ODF
Generate an annotated OpenDocument from a text and list of annotations. Useful to quickly share some annotations.

## Example

```python
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

```

In MS Word:

![alt text](https://raw.githubusercontent.com/ewoij/annotations-to-odf/master/readme_images/helloworld_output.png)

## Dependencies
 - odfpy (tested with 1.3.5)