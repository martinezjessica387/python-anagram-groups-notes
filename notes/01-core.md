# Group words by letter composition: implementation

## What the example does

Sorted casefolded characters form a simple signature. This treats spaces and punctuation as characters and does not perform linguistic normalization.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  "eat",
  "tea",
  "tan",
  "ate",
  "nat"
]
```

Expected result:

```json
[
  [
    "eat",
    "tea",
    "ate"
  ],
  [
    "tan",
    "nat"
  ]
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
