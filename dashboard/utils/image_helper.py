from pathlib import Path


def get_asset_path(*parts):
    """
    Return a safe absolute path inside dashboard/assets.
    """
    base_dir = Path(__file__).resolve().parent.parent
    return (base_dir / "assets").joinpath(*parts)