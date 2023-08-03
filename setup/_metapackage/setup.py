import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-opnsynid-vertical-psychology",
    description="Meta package for open-synergy-opnsynid-vertical-psychology Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_psychology',
        'odoo14-addon-ssi_psychology_case',
        'odoo14-addon-ssi_psychology_case_outsource_work',
        'odoo14-addon-ssi_psychology_consultation',
        'odoo14-addon-ssi_psychology_consultation_outsource_work',
        'odoo14-addon-ssi_psychology_evaluation',
        'odoo14-addon-ssi_psychology_evaluation_operating_unit',
        'odoo14-addon-ssi_psychology_evaluation_outsource_work',
        'odoo14-addon-ssi_psychology_evaluation_related_attachment',
        'odoo14-addon-ssi_psychology_intervention',
        'odoo14-addon-ssi_psychology_operating_unit',
        'odoo14-addon-ssi_psychology_testing',
        'odoo14-addon-ssi_psychology_testing_outsource_work',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
