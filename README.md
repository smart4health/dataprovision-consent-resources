# Smart4Health Data-provision Consent Resources

## Acknowledgements

<img src="./img/eu.jpg" align="left" alt="European Flag" width="60">

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 826117.

## About

The [Smart4Health Data-provision Consent Service](https://github.com/smart4health/dataprovision-consent-service) takes
care of guiding
the citizen through the consent process in
the [Smart4Health MyScience App](https://github.com/smart4health/my-science-app).
The configuration files configured outside this service and served directly as static consent from within this
repository, e.g: https://consents.smart4health.eu/research-consent-en/consent.pdf

## Consents

The two active consents are

- `research-consent-en`
- `research-consent-de`

which will be accessible to the consent service with the consentId

- `smart4health-research-consent-en`
- `smart4health-research-consent-de`

## Yaml Schema validation

To locally validate the yaml files:

Simple yaml validator:

```shell
docker run --rm -it -v $(pwd):/data cytopia/yamllint .  --no-warnings
```

Check the schema:

```shell
pip install -q yml2json jsonschema
python3 yaml_validate.py
```

## PDF Coordinates

When a new PDF needs to be added, we need to calculate the coordinates of the various checkboxes and inputs to insert
text at. To do this, go to the [following url](https://pdfbox.apache.org/download.cgi) and download the first command
line tool (pdfbox-app-<VERSION>.jar). Then, load a specific PDF with the following command:

```shell script
java -jar <path/to/pdfbox-app.jar> PDFDebugger <path/to/pdf>
```

You can then page through the PDF and hover over spots to find out the coordinates. Sometimes the coordinates are not
100% accurate, and you need to play around with them. To try it out locally, the consent services project's signPdfTask
can be used.

Notice that pdf page numbers are 0-indexed.

PDFs should be provided with a ISO compliant export, e.g. PDF/A and at least PDF Version 1.5. Otherwise, inserted texts
could be hidden on some PDF viewers.
