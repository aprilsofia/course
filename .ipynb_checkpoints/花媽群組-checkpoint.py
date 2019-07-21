{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 花媽群組"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "我們這一家，有花媽、花爸、橘子、柚子四個人。花媽腦洞大開想根據不同關係分別開群組，請問花媽最多可以開出多少群組?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "L=['花媽','花爸','橘子','柚子']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from itertools import combinations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "C2 = list(combinations(L, 2))\n",
    "C3 = list(combinations(L, 3))\n",
    "C4 = list(combinations(L, 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([('花媽', '花爸'),\n",
       "  ('花媽', '橘子'),\n",
       "  ('花媽', '柚子'),\n",
       "  ('花爸', '橘子'),\n",
       "  ('花爸', '柚子'),\n",
       "  ('橘子', '柚子')],\n",
       " [('花媽', '花爸', '橘子'),\n",
       "  ('花媽', '花爸', '柚子'),\n",
       "  ('花媽', '橘子', '柚子'),\n",
       "  ('花爸', '橘子', '柚子')],\n",
       " [('花媽', '花爸', '橘子', '柚子')])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C2,C3,C4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C=len(C2+C3+C4)\n",
    "C"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File `花媽群組.py` exists. Overwrite (y/[N])?  y\n",
      "The following commands were written to file `花媽群組.py`:\n",
      "L=['花媽','花爸','橘子','柚子']\n",
      "from itertools import combinations\n",
      "C2 = list(combinations(L, 2))\n",
      "C3 = list(combinations(L, 3))\n",
      "C4 = list(combinations(L, 4))\n",
      "C2,C3,C4\n",
      "C=len(C2+C3+C4)\n",
      "C\n"
     ]
    }
   ],
   "source": [
    "%save \"花媽群組.py\"17 18 22 26 27"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
