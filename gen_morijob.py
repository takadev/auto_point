 i m p o r t   s y s 
 i m p o r t   c o n f i g p a r s e r 
 f r o m   s e l e n i u m   i m p o r t   w e b d r i v e r 
 f r o m   s e l e n i u m . w e b d r i v e r . c o m m o n . a c t i o n _ c h a i n s   i m p o r t   A c t i o n C h a i n s 
 f r o m   s e l e n i u m . w e b d r i v e r . c o m m o n . k e y s   i m p o r t   K e y s 
 f r o m   s e l e n i u m . w e b d r i v e r . s u p p o r t . u i   i m p o r t   W e b D r i v e r W a i t 
 f r o m   s e l e n i u m . w e b d r i v e r . s u p p o r t   i m p o r t   e x p e c t e d _ c o n d i t i o n s   a s   e c 
 f r o m   s e l e n i u m . w e b d r i v e r . s u p p o r t . u i   i m p o r t   S e l e c t 
 f r o m   s e l e n i u m . c o m m o n . e x c e p t i o n s   i m p o r t   N o S u c h E l e m e n t E x c e p t i o n 
 f r o m   t i m e   i m p o r t   s l e e p 
 
 i n i f i l e   =   c o n f i g p a r s e r . S a f e C o n f i g P a r s e r ( ) 
 i n i f i l e . r e a d ( ' / U s e r s / T K / p r o j e c t / a u t o _ p o i n t / c o n f i g . i n i ' ) 
 m a i l   =   i n i f i l e . g e t ( ' s e t t i n g s ' ,   ' i d ' ) 
 p a s s w d   =   i n i f i l e . g e t ( ' s e t t i n g s ' ,   ' p a s s ' ) 
 l o g i n _ u r l   =   " h t t p s : / / s s l . r e a l w o r l d . j p / a u t h / ? s i t e = g e n d a m a _ j p & r i d = & a f = & f r i d = & t o k e n = & g o t o = h t t p % 3 A % 2 F % 2 F w w w . g e n d a m a . j p % 2 F m o r i j o b " 
 
 d r i v e r   =   w e b d r i v e r . C h r o m e ( ' . / c h r o m e d r i v e r ' ) 
 d r i v e r . g e t ( l o g i n _ u r l ) 
 f o r m   =   d r i v e r . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( ' f o r m ' ) [ 0 ] 
 f o r   t a g   i n   f o r m . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( ' i n p u t ' ) : 
 	 i d   =   t a g . g e t _ a t t r i b u t e ( ' i d ' ) 
 	 i f   i d   = =   " r w s i d " : 
 	 	 t a g . s e n d _ k e y s ( m a i l ) 
 	 e l i f   i d   = =   " p a s s " : 
 	 	 t a g . s e n d _ k e y s ( p a s s w d ) 
 
 	 t y p e   =   t a g . g e t _ a t t r i b u t e ( ' t y p e ' ) 
 	 i f   t y p e   = =   ' s u b m i t ' : 
 	 	 t a g . s u b m i t ( ) 
 	 	 b r e a k 
 
 d r i v e r . s w i t c h _ t o . f r a m e ( d r i v e r . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " i f r a m e " ) ) 
 m a i n   =   d r i v e r . f i n d _ e l e m e n t _ b y _ c s s _ s e l e c t o r ( " d i v # m a i n " ) 
 u l _ t a g s   =   m a i n . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( " u l " ) 
 
 l i n k s   =   [ ] 
 f o r   t a g   i n   u l _ t a g s : 
 	 a _ t a g   =   t a g . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " a " ) 
 	 l i n k s . a p p e n d ( s t r ( a _ t a g . g e t _ a t t r i b u t e ( " h r e f " ) ) ) 
 
 p r i n t ( l e n ( l i n k s ) ) 
 f o r   l i n k   i n   l i n k s : 
 	 p r i n t ( l i n k ) 
 	 d r i v e r . g e t ( l i n k ) 
 	 s l e e p ( 1 ) 
 
 	 t r y : 
 	 	 i f r a m e 1   =   d r i v e r . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " i f r a m e " ) 
 	 	 d r i v e r . s w i t c h _ t o . f r a m e ( i f r a m e 1 ) 
 	 e x c e p t   N o S u c h E l e m e n t E x c e p t i o n : 
 	 	 c o n t i n u e 
 	 	 
 	 r e c a p t c h a   =   F a l s e 
 	 t r y : 
 	 	 i f r a m e s   =   d r i v e r . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( " i f r a m e " ) 
 	 	 i f   l e n ( i f r a m e s )   >   0 : 
 	 	 	 d r i v e r . s w i t c h _ t o . f r a m e ( i f r a m e s [ 0 ] ) 
 	 	 	 d i v _ t a g   =   d r i v e r . f i n d _ e l e m e n t _ b y _ c s s _ s e l e c t o r ( " d i v . r e c a p t c h a - c h e c k b o x - c h e c k m a r k " ) 
 	 	 	 d r i v e r . e x e c u t e _ s c r i p t ( " a r g u m e n t s [ 0 ] . c l i c k ( ) ; " ,   d i v _ t a g ) 
 	 	 	 s l e e p ( 1 ) 
 
 	 	 	 d r i v e r . s w i t c h _ t o . w i n d o w ( d r i v e r . w i n d o w _ h a n d l e s [ 0 ] ) 
 	 	 	 i f r a m e 1   =   d r i v e r . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " i f r a m e " ) 
 	 	 	 d r i v e r . s w i t c h _ t o . f r a m e ( i f r a m e 1 ) 
 
 	 	 	 i f r a m e s   =   d r i v e r . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( " i f r a m e " ) 
 
 	 	 	 f o r   t a g   i n   i f r a m e s : 
 	 	 	 	 t i t l e   =   t a g . g e t _ a t t r i b u t e ( " t i t l e " ) 
 	 	 	 	 i f   t i t l e . f i n d ( "x��� " )   >   - 1 : 
 	 	 	 	 	 r e c a p t c h a   =   T r u e 
 	 	 	 	 	 b r e a k 
 
 	 e x c e p t   N o S u c h E l e m e n t E x c e p t i o n : 
 	 	 d r i v e r . s w i t c h _ t o . w i n d o w ( d r i v e r . w i n d o w _ h a n d l e s [ 0 ] ) 
 	 	 i f r a m e 1   =   d r i v e r . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " i f r a m e " ) 
 	 	 d r i v e r . s w i t c h _ t o . f r a m e ( i f r a m e 1 ) 
 
 	 i f   r e c a p t c h a   = =   T r u e : 
 	 	 b r e a k 
 
 	 f o r m   =   d r i v e r . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " f o r m " ) 
 	 i n p u t s   =   f o r m . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( " i n p u t " ) 
 
 	 p r e v _ u r l   =   " " 
 	 f o r   t a g   i n   i n p u t s : 
 	 	 t y p e   =   t a g . g e t _ a t t r i b u t e ( ' t y p e ' ) 
 	 	 i f   t y p e   = =   " s u b m i t " : 
 	 	 	 t a g . s u b m i t ( ) 
 	 	 	 s l e e p ( 1 ) 
 	 	 	 b r e a k 
 
 	 w h i l e   T r u e : 
 	 	 t r y : 
 	 	 	 d r i v e r . s w i t c h _ t o . w i n d o w ( d r i v e r . w i n d o w _ h a n d l e s [ 0 ] ) 
 	 	 	 m a i n   =   d r i v e r . f i n d _ e l e m e n t _ b y _ c s s _ s e l e c t o r ( " d i v . m a i n " ) 
 	 	 	 d r i v e r . s w i t c h _ t o . f r a m e ( m a i n . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " i f r a m e " ) ) 
 	 	 	 f o r m   =   d r i v e r . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " f o r m " ) 
 	 	 	 t a g s   =   f o r m . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( " i n p u t " ) 
 	 	 e x c e p t   N o S u c h E l e m e n t E x c e p t i o n : 
 	 	 	 b r e a k 
 
 	 	 t r y : 
 	 	 	 s e l e c t   =   f o r m . f i n d _ e l e m e n t _ b y _ t a g _ n a m e ( " s e l e c t " ) 
 	 	 	 o p t i o n   =   s e l e c t . f i n d _ e l e m e n t s _ b y _ t a g _ n a m e ( " o p t i o n " ) [ 1 ] 
 	 	 	 s e l e c t _ e l e m e n t   =   S e l e c t ( s e l e c t ) 
 	 	 	 v a l u e   =   s t r ( o p t i o n . g e t _ a t t r i b u t e ( ' v a l u e ' ) ) 
 	 	 	 s e l e c t _ e l e m e n t . s e l e c t _ b y _ v a l u e ( v a l u e ) 
 	 	 e x c e p t   N o S u c h E l e m e n t E x c e p t i o n : 
 	 	 	 p a s s 
 
 	 	 i s _ r a d i o   =   F a l s e 
 	 	 i s _ c h e c k b o x   =   F a l s e 
 	 	 f o r   t a g   i n   t a g s : 
 	 	 	 t y p e   =   t a g . g e t _ a t t r i b u t e ( " t y p e " ) 
 	 	 	 i f   t y p e   = =   " r a d i o "   a n d   i s _ r a d i o   = =   F a l s e : 
 	 	 	 	 d r i v e r . e x e c u t e _ s c r i p t ( " a r g u m e n t s [ 0 ] . c l i c k ( ) ; " ,   t a g ) 
 	 	 	 	 i s _ r a d i o   =   T r u e 
 	 	 	 e l i f     t y p e   = =   " c h e c k b o x "   a n d   i s _ c h e c k b o x   = =   F a l s e : 
 	 	 	 	 d r i v e r . e x e c u t e _ s c r i p t ( " a r g u m e n t s [ 0 ] . c l i c k ( ) ; " ,   t a g ) 
 	 	 	 	 i s _ c h e c k b o x   =   T r u e 
 	 	 	 e l i f   t y p e   = =   " s u b m i t " : 
 	 	 	 	 d r i v e r . e x e c u t e _ s c r i p t ( " a r g u m e n t s [ 0 ] . c l i c k ( ) ; " ,   t a g ) 
 	 	 	 	 s l e e p ( 1 ) 
 	 	 	 	 b r e a k 
 
 d r i v e r . q u i t ( ) 
 
