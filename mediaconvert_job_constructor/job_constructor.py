
class MediaConvertJobConstructor:

    @staticmethod
    def create_crop(x: int, y: int, width: int, height: int):
        return {"X": x, "Y": y, "Width": width, "Height": height}

    def __init__(self, queue_arn: str, role_arn: str, status_update_interval: str = "SECONDS_10", priority: int = 1):
        self.inputs = []
        self.outputs = []
        self.queue_arn = queue_arn
        self.role_arn = role_arn
        self.overlay = None
        self.n = 0
        self.task_token = None
        self.priority = 0
        self.status_update_interval = "SECONDS_10"
        self.acceleration_settings = {
            "Mode": "DISABLED"
        }
        self.settings = {
            "TimecodeConfig": {
                "Source": "ZEROBASED"
            },
            'AdAvailOffset': 0
        }

    def add_task_token(self, task_token: str):
        self.task_token = task_token

    def add_input(self, input_name: str):
        self.inputs.append({"name": input_name})

    def add_overlay(
    self,
    location: str,
    x: int,
    y: int,
    w: int,
    h: int,
    layer: int = 1,
    opacity: int = 50,):
        self.overlay = {
            "InsertableImages": [{
                "Width": w,
                "Height": h,
                "ImageX": x,
                "ImageY": y,
                "Layer": layer,
                "ImageInserterInput": location,
                "Opacity": opacity
            }]
        }

    def add_output(
            self,
            bucket: str,
            output_name: str,
            width: int,
            height: int,
            bitrate: int = 12_000_000,
            crop: dict = None):
        self.outputs.append({"bucket": bucket,
                             "modifier": output_name,
                             "width": width,
                             "height": height,
                             "bitrate": bitrate,
                             "crop": crop})

    def _construct_output_group(self, output: dict):
        self.n += 1
        destination = output['bucket']
        if 's3://' in destination:
            destination = destination.replace('s3://', '')
        group = {
            "Name": f"File Group {self.n}",
            "Outputs": [{
                "ContainerSettings": {
                    "Container": "MP4",
                    "Mp4Settings": {}
                },
                "VideoDescription": {
                    "CodecSettings": {
                        "Codec": "H_264",
                        "H264Settings": {
                            "InterlaceMode": "PROGRESSIVE",
                            "NumberReferenceFrames": 3,
                            "Syntax": "DEFAULT",
                            "Softness": 0,
                            "GopClosedCadence": 1,
                            "GopSize": 90,
                            "Slices": 1,
                            "GopBReference": "DISABLED",
                            "SlowPal": "DISABLED",
                            "EntropyEncoding": "CABAC",
                            "Bitrate": output['bitrate'],
                            "FramerateControl": "INITIALIZE_FROM_SOURCE",
                            "RateControlMode": "CBR",
                            "CodecProfile": "MAIN",
                            "Telecine": "NONE",
                            "MinIInterval": 0,
                            "AdaptiveQuantization": "AUTO",
                            "CodecLevel": "AUTO",
                            "FieldEncoding": "PAFF",
                            "SceneChangeDetect": "ENABLED",
                            "QualityTuningLevel": "SINGLE_PASS",
                            "FramerateConversionAlgorithm": "DUPLICATE_DROP",
                            "UnregisteredSeiTimecode": "DISABLED",
                            "GopSizeUnits": "FRAMES",
                            "ParControl": "INITIALIZE_FROM_SOURCE",
                            "NumberBFramesBetweenReferenceFrames": 2,
                            "RepeatPps": "DISABLED",
                            "DynamicSubGop": "STATIC"
                        }
                    },
                    "AfdSignaling": "NONE",
                    "DropFrameTimecode": "ENABLED",
                    "RespondToAfd": "NONE",
                    "ColorMetadata": "INSERT",
                    "Width": output["width"],
                    "Height": output["height"],
                    "ScalingBehavior": "DEFAULT",
                    "TimecodeInsertion": "DEFAULT",
                    "VideoPreprocessors": {},
                    "AntiAlias": "ENABLED",
                    "Sharpness": 50,
                },
                "AudioDescriptions": [{
                    "AudioTypeControl": "FOLLOW_INPUT",
                    "CodecSettings": {
                        "Codec": "AAC",
                        "AacSettings": {
                            "AudioDescriptionBroadcasterMix": "NORMAL",
                            "Bitrate": 384000,
                            "RateControlMode": "CBR",
                            "CodecProfile": "LC",
                            "CodingMode": "CODING_MODE_2_0",
                            "RawFormat": "NONE",
                            "SampleRate": 48000,
                            "Specification": "MPEG4"
                        }
                    },
                    "LanguageCodeControl": "FOLLOW_INPUT"
                }],
                "NameModifier": output["modifier"],
            }],
            "OutputGroupSettings": {
                "Type": "FILE_GROUP_SETTINGS",
                "FileGroupSettings": {
                    "Destination": f"s3://{destination}/"
                }
            }
        }
        if output["crop"] is not None:
            group["Outputs"][0]["VideoDescription"]["Crop"] = output["crop"]
        return group

    def _construct_input_group(self, input_video: dict):
        return {
            "AudioSelectors": {
                "Audio Selector 1": {
                    "Offset": 0,
                    "DefaultSelection": "DEFAULT",
                    "ProgramSelection": 1
                }
            },
            "VideoSelector": {
                "ColorSpace": "FOLLOW",
                "Rotate": "DEGREE_0",
                "AlphaBehavior": "DISCARD"
            },
            "FilterEnable": "AUTO",
            "PsiControl": "USE_PSI",
            "FilterStrength": 0,
            "DeblockFilter": "DISABLED",
            "DenoiseFilter": "DISABLED",
            "InputScanType": "AUTO",
            "TimecodeSource": "ZEROBASED",
            "FileInput": input_video["name"]
        }

    def create(self):
        job = {}

        if self.task_token:
            task_token1 = self.task_token[0:256]
            task_token2 = self.task_token[256:512]
            task_token3 = self.task_token[512:768]
            job['UserMetadata'] = {
                "TaskToken1": task_token1,
                "TaskToken2": task_token2,
                "TaskToken3": task_token3
            }

        job['Role'] = self.role_arn
        job['Queue'] = self.queue_arn
        job['AccelerationSettings'] = self.acceleration_settings
        job['Priority'] = self.priority
        job['StatusUpdateInterval'] = self.status_update_interval
        job['Settings'] = self.settings
        job['Settings']['Inputs'] = []
        job['Settings']['OutputGroups'] = []


        # add inputs
        for input in self.inputs:
            job["Settings"]["Inputs"].append(
                self._construct_input_group(input))

        # add outputs
        for output in self.outputs:
            group = self._construct_output_group(output)
            if self.overlay:
                group['Outputs'][0]['VideoDescription']['VideoPreprocessors'] = self.overlay
            job["Settings"]["OutputGroups"].append(group)

        return job
