import numpy as np
from typing import Dict
from pathlib import Path

from skimage.morphology import binary_erosion
from infer_subc_2d.utils.file_io import export_inferred_organelle, import_inferred_organelle
from infer_subc_2d.utils.img import apply_mask

##########################
#  infer_cytosol
##########################
def infer_cytosol(nuclei_object: np.ndarray, soma_mask: np.ndarray, erode_nuclei: bool = True) -> np.ndarray:
    """
    Procedure to infer infer from linearly unmixed input. (logical soma AND NOT nucleus)

    Parameters
    ------------
    nuclei_object:
        a 3d image containing the nuclei object
    soma_mask:
        a 3d image containing the soma object (mask)
    erode_nuclei:
        should we erode?

    Returns
    -------------
    cytosol_mask
        boolean np.ndarray

    """
    nucleus_obj = apply_mask(nuclei_object, soma_mask)

    if erode_nuclei:
        cytosol_mask = np.logical_xor(soma_mask, binary_erosion(nuclei_object))
    else:
        cytosol_mask = np.logical_xor(soma_mask, nuclei_object)

    return cytosol_mask


def infer_and_export_cytosol(
    nuclei_object: np.ndarray, soma_mask: np.ndarray, meta_dict: Dict, out_data_path: Path
) -> np.ndarray:
    """
    infer nucleus and write inferred nuclei to ome.tif file

    Parameters
    ------------
    nuclei_object:
        a 3d image containing the nuclei object
    soma_mask:
        a 3d image containing the soma object (mask)
    meta_dict:
        dictionary of meta-data (ome)
    out_data_path:
        Path object where tiffs are written to

    Returns
    -------------
    exported file name

    """
    cytosol = infer_cytosol(nuclei_object, soma_mask)

    out_file_n = export_inferred_organelle(cytosol, "cytosol", meta_dict, out_data_path)
    print(f"inferred cytosol. wrote {out_file_n}")
    return cytosol


def get_cytosol(nuclei_obj: np.ndarray, soma_mask: np.ndarray, meta_dict: Dict, out_data_path: Path) -> np.ndarray:
    """
    load cytosol if it exists, otherwise calculate and write to ome.tif file

    Parameters
    ------------
    in_img:
        a 3d  np.ndarray image of the inferred organelle (labels or boolean)
    soma_mask:
        a 3d image containing the soma object (mask)
    meta_dict:
        dictionary of meta-data (ome)
    out_data_path:
        Path object where tiffs are written to

    Returns
    -------------
    exported file name

    """
    cytosol = import_inferred_organelle("cytosol", meta_dict, out_data_path)

    if cytosol is None:
        cytosol = infer_and_export_cytosol(nuclei_obj, soma_mask, meta_dict, out_data_path)
    else:
        print(f"loaded cytosol from {out_data_path}")

    return cytosol
