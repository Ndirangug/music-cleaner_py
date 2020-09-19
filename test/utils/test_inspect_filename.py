import pytest

from utils.inspect_filename import check_filename_not_useful, FilenameNotUseful


def test_check_filename_not_useful_raises_exception():
    with pytest.raises(FilenameNotUseful):
        filename = "AUD-20200511-WA0000"
        check_filename_not_useful(filename)


@pytest.mark.xfail
def test_check_filename_not_useful_passes():
    with pytest.raises(FilenameNotUseful):
        filename = "Isla-Vista-Worship-Dancing-On-The-Moon-HXLY-KXSS-Remix_kxFU435IWAs"
        check_filename_not_useful(filename)
