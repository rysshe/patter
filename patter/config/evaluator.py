from marshmallow import Schema, fields

from .dataset import DatasetConfig
from .decoder import DecoderConfig


class EvaluatorConfiguration(Schema):
    datasets = fields.Nested(DatasetConfig, load_from="dataset", many=True)
    decoder = fields.Nested(DecoderConfig)

    cuda = fields.Boolean(default=True)
    batch_size = fields.Integer(required=True)
    num_workers = fields.Integer(required=True)
