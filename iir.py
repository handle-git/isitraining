from requests_html import HTMLSession

print(
    "------------------------\n\n    Is it raining?\n\n         "
    + HTMLSession()
    .get(
        "https://isitraining.in/"
        + HTMLSession().get("https://mylocation.org/").text.split("\n")[96][12:-6]
    )
    .text.split("\n ")[69][34:-5]
    + ".\n\n------------------------"
)
