# Reaction-based bot framework

Work-in-progress reaction based bot framework.
Works, but there are many things to do

```python
@react('commit:confirmation', ['Confirm'])
async def co_handler(input, output):
	await output.answerText('commit:continue', """
		Yeah, proceed
	""")

@react('commit:confirmation', ['Cancel'])
async def ca_handler(input, output):
	await output.answerText('beginning', """
		Oh, okay
	""")
```

In this example framework automatically produces bot keyboard 
with `Confirm` and `Cancel` buttons, when entering `commit:confirmation` context


