"""Demo: sine-wave robot arms + bouncing square (DVD screensaver style)."""

import math
import time
from pathlib import Path

import cv2
import numpy as np
import rerun as rr
import rerun.blueprint as rrb
from tqdm import tqdm

URDF_PATH = Path("robot_models/big_yam/big_yam_dual.urdf")
FPS = 60
DURATION = 10  # seconds
N_FRAMES = FPS * DURATION

# DVD-style bouncing square settings
IMG_W, IMG_H = 640, 480
SQUARE_SIZE = 60
SPEED_X, SPEED_Y = 3, 2


def main():
    # --- Rerun setup ---
    blueprint = rrb.Horizontal(
        rrb.Spatial3DView(origin="robot"),
        rrb.Vertical(
            rrb.Spatial2DView(origin="camera_left"),
            rrb.Spatial2DView(origin="camera_right"),
        ),
        column_shares=[3, 1],
    )
    rr.init("interview_demo", spawn=True, default_blueprint=blueprint)

    # --- Load URDF ---
    patched = URDF_PATH.parent / "big_yam_dual_patched.urdf"
    patched.write_text(
        URDF_PATH.read_text().replace('filename="package://', 'filename="')
    )
    rr.log_file_from_path(str(patched), entity_path_prefix="robot", static=True)
    tree = rr.urdf.UrdfTree.from_file_path(str(patched), entity_path_prefix="robot")

    # Joint names for each arm
    left_joints = [f"left_joint{i}" for i in range(1, 7)]
    right_joints = [f"right_joint{i}" for i in range(1, 7)]
    gripper_joints = [
        "left_gripper_l", "left_gripper_r",
        "right_gripper_l", "right_gripper_r",
    ]

    # --- Bouncing square state ---
    sq_x, sq_y = 100.0, 100.0
    dx, dy = float(SPEED_X), float(SPEED_Y)
    colors = [(255, 50, 50), (50, 255, 50), (50, 50, 255),
              (255, 255, 50), (255, 50, 255), (50, 255, 255)]
    color_idx = 0

    # --- Animate ---
    for frame in tqdm(range(N_FRAMES), desc="Animating", unit="frame"):
        t = frame / FPS
        rr.set_time("time", duration=t)

        # Sine wave on joints (different phase per joint)
        for j, name in enumerate(left_joints):
            angle = 0.5 * math.sin(2 * math.pi * 0.5 * t + j * 0.8)
            joint = tree.get_joint_by_name(name)
            rr.log(f"robot/joints/{name}", joint.compute_transform(angle, clamp=False))

        for j, name in enumerate(right_joints):
            angle = 0.5 * math.sin(2 * math.pi * 0.5 * t + j * 0.8 + math.pi)
            joint = tree.get_joint_by_name(name)
            rr.log(f"robot/joints/{name}", joint.compute_transform(angle, clamp=False))

        # Grippers open/close with sine wave
        grip = 0.04 + 0.04 * math.sin(2 * math.pi * 0.3 * t)
        for name in gripper_joints:
            joint = tree.get_joint_by_name(name)
            rr.log(f"robot/joints/{name}", joint.compute_transform(grip, clamp=False))

        # --- DVD bouncing square ---
        sq_x += dx
        sq_y += dy
        bounced = False
        if sq_x <= 0 or sq_x + SQUARE_SIZE >= IMG_W:
            dx = -dx
            bounced = True
        if sq_y <= 0 or sq_y + SQUARE_SIZE >= IMG_H:
            dy = -dy
            bounced = True
        if bounced:
            color_idx = (color_idx + 1) % len(colors)

        img_left = np.zeros((IMG_H, IMG_W, 3), dtype=np.uint8)
        cv2.rectangle(
            img_left,
            (int(sq_x), int(sq_y)),
            (int(sq_x + SQUARE_SIZE), int(sq_y + SQUARE_SIZE)),
            colors[color_idx],
            -1,
        )
        rr.log("camera_left", rr.Image(img_left))

        # Mirror for right camera
        img_right = np.flip(img_left, axis=1).copy()
        rr.log("camera_right", rr.Image(img_right))

    patched.unlink(missing_ok=True)
    print("\nDone! Sent all frames to Rerun.")


if __name__ == "__main__":
    main()
