import cv2

class CustomWallpaper:
    def __init__(self, path, number_of_rect):
        self.path = path
        self.number_of_rect = number_of_rect

    def save_image(self, image):
        cv2.imwrite(f"{self.path}_result.png", image)
        print("image save")

    def blur(self, image, kernel_size):
        blur = cv2.blur(image, (kernel_size, kernel_size))
        return blur

    def replace_rect(self, blr_img, org_img, x, y, w, h):
        result = blr_img.copy()
        result[y:y + h, x:x + w] = org_img[y:y + h, x:x + w]
        return result

    def space_bet_rect(self, number_of_rect, w):
        if number_of_rect == 1:
            return 0
        elif number_of_rect <= 6:
            x_rect = w - (2 * (0.1 * w))
            x = (x_rect * 0.2) // (number_of_rect - 1)
            return x
        else:
            print('------------------------------------------------------------------')
            print('Error : your number of rect is too high(it must be between 1 to 6)')
            print('------------------------------------------------------------------')

    def find_rect_pos(self, number_of_rect, space_bet: int, w, h):

        pad_w = w * 0.1
        pad_h = h * 0.1

        inner_w = w - (2 * pad_w)
        all_spc_btw_rects = (space_bet * (number_of_rect - 1))

        h_rect = h - 2 * pad_h
        w_rect = (inner_w - all_spc_btw_rects) / number_of_rect

        rects = [(int(pad_w), int(pad_h), int(w_rect), int(h_rect))]

        for _ in range(number_of_rect - 1):
            x = rects[-1][0] + w_rect + space_bet
            rects += [(int(x), int(pad_h), int(w_rect), int(h_rect))]

        return rects

    def run(self):
        print("making walpaper start ...")
        org_img = cv2.imread(self.path)
        blr_img = self.blur(org_img, 20)
        h, w, _ = org_img.shape
        bet = self.space_bet_rect(self.number_of_rect, w)
        rects = self.find_rect_pos(self.number_of_rect, bet, w, h)
        res_img = blr_img.copy()
        for rect in rects:
            res_img = self.replace_rect(res_img, org_img, rect[0], rect[1], rect[2], rect[3])
        self.save_image(res_img)
        print("making walpaper finish")
