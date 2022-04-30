#include QMK_KEYBOARD_H
#include "keymap_steno.h"

#define STENO       0
#define QWERTY_1    1
#define QWERTY_2    2
#define PUNCTUATION 3
#define FUNCTION    4

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    // Main layer, everything goes through here
    [STENO] = LAYOUT_georgi(
        TG(1)  , STN_S1 , STN_TL , STN_PL , STN_HL , STN_ST1,    STN_ST3, STN_FR , STN_PR , STN_LR , STN_TR , STN_DR ,
        STN_PWR, STN_S2 , STN_KL , STN_WL , STN_RL , STN_ST2,    STN_ST4, STN_RR , STN_BR , STN_GR , STN_SR , STN_ZR ,
                                   STN_N1 , STN_A  , STN_O  ,    STN_E  , STN_U  , STN_N2
    ),
    [QWERTY_1] = LAYOUT_georgi(
        TO(0)  , KC_Q   , KC_W   , KC_E   , KC_R   , KC_T   ,    KC_Y   , KC_U   , KC_I   , KC_O   , KC_P   , KC_DEL ,
        KC_LSFT, KC_A   , KC_S   , KC_D   , KC_F   , KC_G   ,    KC_H   , KC_J   , KC_K   , KC_L   , KC_SCLN, KC_QUOT,
                                   KC_LCTL, KC_ENT , KC_BSPC,    KC_TAB , KC_SPC , LT(QWERTY_2, KC_ESC)
    ),
    [QWERTY_2] = LAYOUT_georgi(
        _______, KC_1   , KC_2   , KC_3   , KC_4   , KC_5   ,    KC_6   , KC_7   , KC_8   , KC_9   , KC_0   , KC_DEL ,
        TG(3)  , KC_Z   , KC_X   , KC_C   , KC_V   , KC_B   ,    KC_N   , KC_M   , KC_COMM, KC_DOT , KC_SLSH, KC_QUOT,
                                   KC_LALT, KC_LWIN, _______,    _______, _______, _______
    ),
    [PUNCTUATION] = LAYOUT_georgi(
        TO(1)  , _______, _______, KC_MINS, KC_EQL , KC_GRV ,    KC_PGUP, KC_HOME, KC_UP  , KC_END , _______, _______,
        _______, _______, _______, KC_LBRC, KC_RBRC, KC_BSLS,    KC_PGDN, KC_LEFT, KC_DOWN, KC_RGHT, _______, _______,
                                   _______, _______, _______,    _______, _______, LT(FUNCTION, KC_ESC)
    ),
    [FUNCTION] = LAYOUT_georgi(
        _______, _______, _______, _______, _______, _______,    KC_F1  , KC_F2  , KC_F3  , KC_F4  , KC_F5  , KC_F6  ,
        _______, _______, _______, KC_CAPS, KC_PSCR, _______,    KC_F7  , KC_F8  , KC_F9  , KC_F10 , KC_F11 , KC_F12 ,
                                   _______, _______, _______,    _______, _______, _______
    ),
};

// Don't fuck with this, thanks.
// will do jane :thumbsup:
size_t keymapsCount  = sizeof(keymaps)/sizeof(keymaps[0]);
