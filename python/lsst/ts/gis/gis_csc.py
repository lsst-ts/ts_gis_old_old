import asyncio

class gisCSC(salobj.ConfigurableCsc):
    """Global Interlock System CSC

    """

    def __init__(
        self,
        config_dir=None,
        initial_state=salobj.State.STANDBY,
        simulation_mode=0
    ):

        schema_path = (
            pathlib.Path(__file__)
            .resolve()
            .parents[4]
            .joinpath("schema","gis.yaml")
        )


        super().__init__(
        "ATDome",
        index=0,


    )