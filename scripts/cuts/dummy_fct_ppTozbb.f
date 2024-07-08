      logical FUNCTION dummy_cuts(P)
C**************************************************************************
C     INPUT:
C            P(0:3,1)           MOMENTUM OF INCOMING PARTON
C            P(0:3,2)           MOMENTUM OF INCOMING PARTON
C            P(0:3,3)           MOMENTUM OF ...
C            ALL MOMENTA ARE IN THE REST FRAME!!
C            COMMON/JETCUTS/   CUTS ON JETS
C     OUTPUT:
C            TRUE IF EVENTS PASSES ALL CUTS LISTED
C**************************************************************************
      IMPLICIT NONE
c
c     Constants
c
      include 'genps.inc'
      include 'nexternal.inc'
C
C     ARGUMENTS
C
      REAL*8 P(0:3,nexternal)
C
C     PARAMETERS
C
      real*8 PI
      parameter( PI = 3.14159265358979323846d0 )
c
c     particle identification
c
      LOGICAL  IS_A_J(NEXTERNAL),IS_A_L(NEXTERNAL)
      LOGICAL  IS_A_B(NEXTERNAL),IS_A_A(NEXTERNAL),IS_A_ONIUM(NEXTERNAL)
      LOGICAL  IS_A_NU(NEXTERNAL),IS_HEAVY(NEXTERNAL)
      logical  do_cuts(nexternal)
      COMMON /TO_SPECISA/IS_A_J,IS_A_A,IS_A_L,IS_A_B,IS_A_NU,IS_HEAVY,
     . IS_A_ONIUM, do_cuts
c
      REAL*8 PB(0:3,0:1)  ! the momentum of b quarks
      REAL*8 PBT(0:3,0:1) ! the momentum of b~quarks
      integer k           ! index on momentum components
      integer l           ! index on final state particles
      integer m1          ! index on momentum of b quarks components
      integer m2          ! index on momentum of b~ quarks components
      REAL*8 PTOT(0:3)    ! ptot of the final state
      REAL*8 PTOT1(0:3)   ! ptot of the system bb~
      REAL*8 themass      ! inv mass of the final state
      REAL*8 themass1     ! inv mass of the system bb~
      logical in1
      integer i,j
c
      include 'maxamps.inc'
      integer idup(nexternal,maxproc,maxsproc)
      integer mothup(2,nexternal)
      integer icolup(2,nexternal,maxflow,maxsproc)
      include 'leshouche.inc'
c
      dummy_cuts=.true.
c
c     cut on the final state mass
      do j=0,3
         ptot(j)=0d0
      enddo
      do i=1,nexternal
         if(is_heavy(i).or.is_a_b(i))then
            do j=0,3
               ptot(j)=ptot(j)+p(j,i)
            enddo
         endif
      enddo
c
      themass=sqrt(ptot(0)**2-ptot(1)**2-ptot(2)**2-ptot(3)**2)
      if(themass.lt.1100d0)then
         dummy_cuts=.false.
         return
      endif
c
c     cut on the pair bb~ masses
      do k=0,3
         ptot1(k)=0d0
      enddo
      m1=0
      m2=0
      do l=1,nexternal
         if(idup(l,1,1).eq.5)then
            do k=0,3
               pb(k,m1)=p(k,l)
            enddo
            m1=m1+1
         elseif(idup(l,1,1).eq.-5)then
            do k=0,3
               pbt(k,m2)=p(k,l)
            enddo
            m2=m2+1
         endif
      enddo
c
c     consistency check
      if(m1.gt.1.or.m2.gt.1) then
         write(*,*)' found too many bs!',m1,m2
         stop
      endif
c
      do k=0,3
         ptot1(k)=pb(k,0)+pbt(k,0)
      enddo
      themass1=sqrt(ptot1(0)**2-ptot1(1)**2-ptot1(2)**2-ptot1(3)**2)
c
      in1=themass1.gt.105d0.and.themass1.lt.145d0
c      
      if(.not.in1)then
         dummy_cuts=.false.
         return
      endif
c
      return
      end

      subroutine get_dummy_x1(sjac, X1, R, pbeam1, pbeam2, stot, shat)
      implicit none
      include 'maxparticles.inc'
      include 'run.inc'
c      include 'genps.inc'
      double precision sjac ! jacobian. should be updated not reinit
      double precision X1   ! bjorken X. output
      double precision R    ! random value after grid transfrormation. between 0 and 1
      double precision pbeam1(0:3) ! momentum of the first beam (input and/or output)
      double precision pbeam2(0:3) ! momentum of the second beam (input and/or output)
      double precision stot        ! total energy  (input and /or output)
      double precision shat        ! output

c     global variable to set (or not)
      double precision cm_rap
      logical set_cm_rap
      common/to_cm_rap/set_cm_rap,cm_rap
      
      set_cm_rap=.false. ! then cm_rap will be set as .5d0*dlog(xbk(1)*ebeam(1)/(xbk(2)*ebeam(2)))
                         ! ebeam(1) and ebeam(2) are defined here thanks to 'run.inc'
      shat = x1*ebeam(1)*ebeam(2)
      return 
      end

      subroutine get_dummy_x1_x2(sjac, X, R, pbeam1, pbeam2, stot,shat)
      implicit none
      include 'maxparticles.inc'
      include 'run.inc'
c      include 'genps.inc'
      double precision sjac ! jacobian. should be updated not reinit
      double precision X(2)   ! bjorken X. output
      double precision R(2)    ! random value after grid transfrormation. between 0 and 1
      double precision pbeam1(0:3) ! momentum of the first beam
      double precision pbeam2(0:3) ! momentum of the second beam
      double precision stot        ! total energy
      double precision shat        ! output

c     global variable to set (or not)
      double precision cm_rap
      logical set_cm_rap
      common/to_cm_rap/set_cm_rap,cm_rap
      
      set_cm_rap=.false. ! then cm_rap will be set as .5d0*dlog(xbk(1)*ebeam(1)/(xbk(2)*ebeam(2)))
                         ! ebeam(1) and ebeam(2) are defined here thanks to 'run.inc'
      shat = x(1)*x(2)*ebeam(1)*ebeam(2)
      return 
      end


      logical  function dummy_boostframe()
      implicit none
c
c      
      dummy_boostframe = .false.
      return
      end
      
