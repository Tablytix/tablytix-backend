import uuid
import layoutparser as lp
from PIL import Image

model = lp.Detectron2LayoutModel(
    config_path='model/config.yaml',
    model_path='model/model.pth',
    label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"},
    extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8]
)


def layout_analysis(file):
    image = Image.open(file)
    layout = model.detect(image)

    filename = str(uuid.uuid4())

    result = lp.draw_box(image, layout, box_width=3,
                         show_element_id=True, show_element_type=True)
    result.save(f"uploads/{filename}.png")

    return filename